import streamlit as st
import argparse
import json


def read_articles(filename):

    with open(filename, 'r', encoding="utf-8") as f:
        data = json.load(f)
    return data


def get_inputs(hints):

    keys = []
    i = 0
    for hint in hints:
        user_input = st.text_input(f"请输入{hint}：")
        keys.append(user_input)
    flag = 1
    flag = st.text_input("当你全部确认以后请输入0")
    keysandflag = [keys, flag]
    return keysandflag


def replace(article, keys):

    for i in range(len(keys)):
        article = article.replace(f"{{{{{i + 1}}}}}", keys[i])
        # TODO: 将 article 中的 {{i}} 替换为 keys[i]
        # hint: 你可以用 str.replace() 函数，也可以尝试学习 re 库，用正则表达式替换
    return article


def execute_after_all(result):
    st.write(result)


if __name__ == "__main__":
    # 标题
    st.title("填字游戏")
    st.write("欢迎使用")
    # 地址
    file = st.text_input("请输入你文章所在的地址")
    st.write("你好，你输入的地址是", file)
    data = read_articles(file)
    # 第几篇
    articles = data["articles"]
    articles_num =len(articles)
    st.write("你好，你输入的地址文章的数量是", articles_num)
    num = st.text_input("请输入你文章的序号,从零开始")
    # TODO: 根据参数或随机从 articles 中选择一篇文章
    articles = articles[int(num)]
    # TODO: 给出合适的输出，提示用户输入
    keys = get_inputs(articles["hints"])
    # TODO: 获取用户输入并进行替换
    article = replace(articles["article"], keys[0])
    # TODO: 给出结果
    if int(keys[1]) is 0:
        execute_after_all(article)




