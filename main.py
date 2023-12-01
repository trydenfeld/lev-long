entry_total = float(input("Entry Total: $"))
entry_price  = float(input("Entry Price: $"))
leverage = float(input("Enter X leverage:"))
long_short = (input("Enter l for long or s for short:"))
profit_target = float(input("Enter Profit Target: $"))

size = (entry_total/entry_price) * leverage
value = size * entry_price
long_sell = (value + profit_target) / size
short_sell = (value - profit_target) / size


margin = 1/leverage
liq_long = entry_price * (1-margin)
liq_short = entry_price * (1+margin)


print(f"\nLong liquidation at ${liq_long:.6f}") if long_short == "l" else print(f"\nShort liquidation at ${liq_short:.6f}\n")

print(f"\nFor ${profit_target} profit, sell at")
print(f"${long_sell:.6f}") if long_short == "l" else print(f"${short_sell:.6f}")
