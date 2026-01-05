from fastapi import FastAPI, HTTPException, status, Path
from pydantic import BaseModel
from typing import Dict, Optional

app = FastAPI()

users= {
    1: {
        "account_holder": "Rahul",
        "balance": 5000,
    }
}
class BankAccount(BaseModel):
    account_holder: str
    balance: float

class UpdateAccount(BaseModel):
    account_holder: Optional[str] = None
    balance: Optional[float] = None


@app.get("/")
def root():
    return {"message": "Welcome to Banking System API"}


@app.get("/accounts/{account_number}")
def get_account(
    account_number: int = Path(..., gt=0, description="Enter valid account ID")
):
    if account_number not in users:
        raise HTTPException(404, "Account not found")
    return users[account_number]


@app.post("/accounts/{account_number}", status_code=status.HTTP_201_CREATED)
def add_account(account_number: int, account: BankAccount):
    if account_number in users:
        raise HTTPException(400, "Account already exists")

    if account.balance < account.minimum_balance:
        raise HTTPException(400, "Initial balance below minimum balance")

    users[account_number] = account.dict()
    return users[account_number]


@app.put("/accounts/{account_number}")
def update_account(account_number: int, account: UpdateAccount):
    if account_number not in users:
        raise HTTPException(404, "Account not found")

    if account.account_holder is not None:
        users[account_number]["account_holder"] = account.account_holder

    if account.balance is not None:
        if account.balance < users[account_number]["minimum_balance"]:
            raise HTTPException(400, "Balance below minimum balance")
        users[account_number]["balance"] = account.balance

    return users[account_number]


@app.delete("/accounts/{account_number}")
def delete_account(account_number: int):
    if account_number not in users:
        raise HTTPException(404, "Account not found")

    deleted_account = users.pop(account_number)
    return {
        "message": "Account deleted successfully",
        "deleted_account": deleted_account
    }


@app.post("/accounts/{account_number}/deposit")
def deposit(account_number: int, amount: float):
    if account_number not in users:
        raise HTTPException(404, "Account not found")

    if amount <= 0:
        raise HTTPException(400, "Deposit amount must be positive")

    users[account_number]["balance"] += amount
    return {
        "message": "Deposit successful",
        "balance": users[account_number]["balance"]
    }


@app.post("/accounts/{account_number}/withdraw")
def withdraw(account_number: int, amount: float):
    if account_number not in users:
        raise HTTPException(404, "Account not found")

    account = users[account_number]

    if amount <= 0:
        raise HTTPException(400, "Withdrawal amount must be positive")

    if account["balance"] - amount < account["minimum_balance"]:
        raise HTTPException(400, "Minimum balance violation")

    account["balance"] -= amount
    return {
        "message": "Withdrawal successful",
        "balance": account["balance"]
    }

@app.get("/total-balance")
def total_balance():
    if not users:
        raise HTTPException(400, "No accounts available")

    total = sum(acc["balance"] for acc in users.values())
    return {"total_balance": total}


