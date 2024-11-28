import tkinter as tk
from tkinter import ttk


def submit_form():
    name = name_entry.get()
    age = age_entry.get()
    gender = gender_var.get()
    output_label.config(text=f"姓名: {name}, 年龄: {age}, 性别: {gender}")


# 创建主窗口
root = tk.Tk()
root.title("用户信息表单")
root.geometry("400x300")
root.configure(bg="#f5f5f5")  # 设置背景颜色

# 标题
title_label = tk.Label(root, text="用户信息表单", font=("Helvetica", 18, "bold"), bg="#f5f5f5", fg="#333")
title_label.pack(pady=10)

# 名字输入
name_frame = tk.Frame(root, bg="#f5f5f5")
name_frame.pack(pady=5)
name_label = tk.Label(name_frame, text="姓名:", font=("Arial", 12), bg="#f5f5f5")
name_label.pack(side=tk.LEFT, padx=5)
name_entry = ttk.Entry(name_frame, font=("Arial", 12))
name_entry.pack(side=tk.LEFT)

# 年龄输入
age_frame = tk.Frame(root, bg="#f5f5f5")
age_frame.pack(pady=5)
age_label = tk.Label(age_frame, text="年龄:", font=("Arial", 12), bg="#f5f5f5")
age_label.pack(side=tk.LEFT, padx=5)
age_entry = ttk.Entry(age_frame, font=("Arial", 12))
age_entry.pack(side=tk.LEFT)

# 性别选择
gender_frame = tk.Frame(root, bg="#f5f5f5")
gender_frame.pack(pady=5)
gender_label = tk.Label(gender_frame, text="性别:", font=("Arial", 12), bg="#f5f5f5")
gender_label.pack(side=tk.LEFT, padx=5)
gender_var = tk.StringVar(value="男")
male_radio = ttk.Radiobutton(gender_frame, text="男", variable=gender_var, value="男")
female_radio = ttk.Radiobutton(gender_frame, text="女", variable=gender_var, value="女")
male_radio.pack(side=tk.LEFT, padx=5)
female_radio.pack(side=tk.LEFT, padx=5)

# 提交按钮
submit_button = ttk.Button(root, text="提交", command=submit_form)
submit_button.pack(pady=15)

# 输出区域
output_label = tk.Label(root, text="", font=("Arial", 12), bg="#f5f5f5", fg="#007BFF")
output_label.pack(pady=5)

# 运行主循环
root.mainloop()
