import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales_2025 = [120, 150, 170, 160, 200, 230]
sales_2026 = [140, 160, 190, 210, 220, 260]

plt.figure(figsize=(8,4)) # w,h in inches
plt.plot(months,sales_2025, marker= "o", label="2025")
plt.plot(months,sales_2026, marker= "s", label="2026")

plt.title("Monthly Sales")
plt.xlabel("Months")
plt.ylabel("Units Sold")

plt.grid(True, alpha = 0.3)
plt.legend()
# plt.savefig("sales_chart1_.jpg")
plt.savefig("sales_chart1_.jpg", dpi=1300, bbox_inches="tight")
# plt.show()