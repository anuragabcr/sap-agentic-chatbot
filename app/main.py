from graph.graph import agent

while True:
    query = input("User: ")
    result = agent.invoke({"query": query})
    print("Assistant:", result["response"])
