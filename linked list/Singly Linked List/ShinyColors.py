import Group_Linked_list as gll
import Group as g

group_linked = gll.Group_Linked_list()    # 宣告 Group_Linked_list 變數
group_linked.head = g.Group("illumination  STARS")    # 設定 Group_Linked_list 變數 head的值
#print(group_linked.head.name)

antica = g.Group("L'Antica")    # 新增 3 個Group節點
alstroe = g.Group("ALSTROEMERIA")
hokako = g.Group("放課後クライマックスガールズ")
antica.next = alstroe    # 將Group節點連接一起
alstroe.next = hokako

group_linked.head.next = antica    # 將新的Group節點串列接到head後
print("初始的Linked list: ")
group_linked.print_list()    # 印出 Group_Linked_list 的所有數值

"""
---------- 實作 add_beginning(self, new_name) ----------
新增 "Straylight" 到第一個節點
"""
print("新增 Straylight 到第一個節點後的Linked list: ")
group_linked.add_beginning("Straylight")
group_linked.print_list()

"""
---------- 實作 add_ending(self, new_name) ----------
新增 "noctchill" 到最後一個節點
"""
print("新增 noctchill 到第一個節點後的Linked list: ")
group_linked.add_ending("noctchill")
group_linked.print_list()

# 宣告新的Group_Linked_list變數來測試Linked list為空的狀況
# new_group_linked = gll.Group_Linked_list()    
# new_group_linked.add_ending("noctchill")
# new_group_linked.print_list()

"""
---------- 實作 add_ending(self, new_name) ----------
新增 "SHHis" 到L'Antica後
"""
print("新增 SHHis 到L'Antica後: ")
group_linked.add_between(antica, "SHHis")
group_linked.print_list()

"""
---------- 實作 remove_node(self, rmname) ----------
新增 "ml" 到 ALSTROEMERIA 後，再刪除 "ml"
"""
print("新增 ml 到 ALSTROEMERIA 後: ")
group_linked.add_between(alstroe, "ml")
group_linked.print_list()
print("刪除 ml: ")
group_linked.remove_node("ml")
group_linked.print_list()