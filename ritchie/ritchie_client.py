"""The Python implementation of the GRPC ritchie.Ritchie client."""

import logging
import grpc
import inquirer
import ritchie_pb2
import ritchie_pb2_grpc


def run():
    
    # Configure channel
    channel = grpc.insecure_channel('localhost:50051')
    stub = ritchie_pb2_grpc.RitchieStub(channel)
    
    # Ask for inputs (prompt)
    name = input("Enter your name: ") 
    
    question2 = [
    inquirer.List('boolean',
                message = "Have you ever used Ritchie?",
                choices = ["true", "false"],
            ),
    ]
    q2_answer = inquirer.prompt(question2)
    boolean = q2_answer["boolean"]
    
    question3 = [
    inquirer.List('automate',
                message = "What do you want to automate?",
                choices = ["daily tasks", "workflows", "toils", "everything"],
            ),
    ]
    q3_answer = inquirer.prompt(question3)
    automate = q3_answer["automate"]
    
    text = input("Type some text: ") 
    
    # Call the Ritchie method from the ritchie.proto file with inputs
    response = stub.Ritchie(ritchie_pb2.RitchieRequest(name=name, boolean=boolean, automate=automate, text=text))
    print("\n\033[36m💡 Ritchie formula execution returned by server:\033[0m\n\n" + response.message)


if __name__ == '__main__':
    logging.basicConfig()
    run()
