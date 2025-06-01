import xml.etree.ElementTree as ET

# tree = ET.parse('/Users/songzhao/code/project/Pndroid/main_activity.xml')
# root = tree.getroot()  # 获取根元素
#
# print(f"root: {root.tag}, 属性:{root.attrib}")
# # 遍历子元素
# for child in root:
#     print(f"标签名: {child.tag}, 属性: {child.attrib}")
#     if 'name' in child.attrib:
#         print(f"姓名: {child.attrib['name']}")
#     print(f"文本内容: {child.text}")


def get_root(path):
    tree = ET.parse(path)
    return tree.getroot()
