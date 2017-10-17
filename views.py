from auction import Auction

@Auction.route('/')
def index():
  return '<h1>index</h1>

# Login
# Logout

## GLOBAL
# Admin (organization)
# Manage Users and Roles
# Manage Auctions

## By Auction
## Pre
# Manage Donors (bulk copy)
# Manage Customers (bulk copy)
# Manage Donations (items)
# Manage Tables (Names, item assignments)
# Bid sheets

## Active
# Check-in Customer
# Check-out Customer
# Manage Bids
# Open/Close Tables

## Post
# Close Auction
# Bill unpaid Customers

## Reports
