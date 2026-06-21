from services.rag_service import query_rag


print("AI Academic Assistant Started")
print("Type exit to stop")


while True:

    question = input("\nYou: ")


    if question.lower()=="exit":
        break


    answer = query_rag(question)


    print("\nAI:", answer)