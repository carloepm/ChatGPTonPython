import openai
import config
import typer
from rich import print
from rich.table import Table


def main(): 

    openai.api_key = config.api_key

    print("[bold green]ChatGPT App Python\b")

    table = Table("Comando", "Descripcion")
    table.add_row("exit", "Salir de la app")
    table.add_row("new", "Crear nueva conversacion")
    print(table)


#contexto del asistente

    [context] = [{'role': 'system', 'content': 'Eres un asistente util.'}]

    messages = [context]
#A continuacion va el codigo que generaria la pregunta al ChatGPT.
    
    while True:


        content = __prompt()

        if content == 'new':
            print('Nueva conversacion creada')
            messages = [context]
            content = __prompt()

        messages.append({'role': 'user', 'content': content})

        response = openai.ChatCompletion.create(model='gpt-3.5-turbo',
                             messages=messages)
    
        response_context = response.choices[0].message.content
    
# contexto de todas las preguntas y respuestas

        messages.append({'role': 'assistant', 'content': response_context})


#Aqui se realiza la respuesta, agregando choises, message y content limito al codigo y al chat a que ejecute
#unicamente la respuesta que yo deseo

        print(f"[bold green]> \b[green]{response_context}[/green]")

def __prompt() -> str:
    prompt = typer.prompt("\nCual es tu pregunta? ")

    if prompt == 'exit':
        exit = typer.confirm('✋ tas seguro?') 
        if exit:
            print('Chau!')
            raise typer.Abort()
        
        return __prompt()

    return prompt



if __name__ == "__main__":
    typer.run(main)
