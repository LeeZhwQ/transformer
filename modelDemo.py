from transformers import pipeline

# 初始化问答模型
qa_model = pipeline("question-answering", model="uer/roberta-base-chinese-extractive-qa")

# 示例用法
def ask_question(context,question):
    answer = qa_model(question=question,context=context)
    return{
        "答案": answer['answer'],
        "置信度" : answer['score'],
        "起始位置":answer['start'],
        "结束位置":answer['end']
    }


# 示例上下文和问题
context = "北京是中国的首都，有着3000多年的建城史和860多年的建都史。"
question = "北京有多少年的建都史？"

# 获取答案并输出
answer = ask_question(context, question)
print(f"问题：{question}")
print(f"上下文：{context}")
print("答案详情：")
for k, v in answer.items():
    print(f"{k}: {v}")

# 交互式版本（取消注释使用）
# while True:
#     try:
#         print("\n输入新的上下文（直接回车使用当前上下文）：")
#         new_context = input().strip()
#         if new_context:
#             context = new_context
#         question = input("请输入问题（输入q退出）：").strip()
#         if question.lower() == "q":
#             break
#         answer = ask_question(context, question)
#         print("\n回答：")
#         for k, v in answer.items():
#             print(f"{k}: {v}")
#     except KeyboardInterrupt:
#         break