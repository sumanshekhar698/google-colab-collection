import numpy as np
import matplotlib.pyplot as plt

np.random.seed(49)
study_hours = np.random.uniform(1,10,50)

exam_marks = study_hours * 8 + np.random.normal(0,5,50) + 5

plt.figure(figsize=(6,5))

plt.scatter(study_hours,exam_marks, c=exam_marks, cmap="viridis")
plt.colorbar(label="score")

plt.title("Marks Distribution")
plt.xlabel("hours")
plt.ylabel("marks")

plt.savefig("marks_distribution_.jpg", dpi=1300, bbox_inches="tight")
plt.show()



