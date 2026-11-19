import numpy as np
import matplotlib.pyplot as plt


fig, axes =  plt.subplots(1,2, figsize=(12,5))


axes[0].hist(np.random.normal(70, 10,1500), bins =  10, color="salmon", edgecolor="white" )
axes[0].set_title("500 Marks Distribution")
axes[0].set_xlabel("Marks")


axes[1].pie([400, 30, 20, 10], labels=["Python","Web Dev", "Data Science", "AI"], autopct="%1.1f%%", startangle= 90)
axes[1].set_title("Subject Distribution")


plt.tight_layout()
plt.savefig("mix_chart.jpg", dpi=1300, bbox_inches="tight")
plt.show()



