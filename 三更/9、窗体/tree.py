import customtkinter as ctk
from tkinter import ttk

# 初始化 CustomTkinter
ctk.set_appearance_mode("Dark")  # 主题：Light, Dark, System
ctk.set_default_color_theme("blue")  # 主题颜色：blue, dark-blue, green


def on_item_select(event):
    selected_item = tree.selection()
    item_text = tree.item(selected_item, "text")
    info_label.configure(text=f"选中的项: {item_text}")


# 创建主窗口
root = ctk.CTk()
root.title("树形组件示例")
root.geometry("600x400")

# 标题
title_label = ctk.CTkLabel(root, text="树形组件示例", font=("Helvetica", 20, "bold"))
title_label.pack(pady=10)

# 创建树形组件
tree_frame = ctk.CTkFrame(root)
tree_frame.pack(pady=10, fill="both", expand=True, padx=20)

# 使用 ttk.Treeview 来创建树形组件
tree = ttk.Treeview(tree_frame, columns=("value"), show="tree headings")
tree.heading("#0", text="名称", anchor="w")
tree.heading("value", text="描述", anchor="w")

# 添加示例数据
tree.insert("", "end", text="父节点 1", values=("描述 1"))
tree.insert("", "end", text="父节点 2", values=("描述 2"))
child1 = tree.insert("", "end", text="父节点 3", values=("描述 3"))
tree.insert(child1, "end", text="子节点 3.1", values=("描述 3.1"))
tree.insert(child1, "end", text="子节点 3.2", values=("描述 3.2"))

# 配置滚动条
tree_scroll = ttk.Scrollbar(tree_frame, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=tree_scroll.set)
tree_scroll.pack(side="right", fill="y")
tree.pack(side="left", fill="both", expand=True)

# 绑定选择事件
tree.bind("<<TreeviewSelect>>", on_item_select)

# 显示选中信息
info_label = ctk.CTkLabel(root, text="选中的项: 无", font=("Arial", 14))
info_label.pack(pady=10)

# 运行主循环
root.mainloop()
