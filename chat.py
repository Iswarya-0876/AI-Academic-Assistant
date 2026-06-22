from services.rag_service import answer



while True:


    question=input(
        "\nYou: "
    )


    if question=="exit":

        break



    response=answer(
        question
    )


    print(
        "\nAI:",
        response
    )