import matplotlib.pyplot as plt


languages = ["Python", "JavaScript", "Java", "C++", "Go"]
students = [45, 30, 20, 15, 10]


plt.figure(figsize=(8,4)) # w,h in inches
bars = plt.bar(languages, students, color="skyblue", edgecolor="navy")
plt.bar_label(bars)

plt.title("P Language Distribution")
plt.ylabel("Number of Students")

plt.show()