# Como rodar o Chatbot Flask com OpenAI

1. Instale as dependências (já feito):
   - flask
   - openai
   - python-dotenv

  ```bash
   pip install numpy openai python-dotenv tiktoken flask opencv-python
```


2. Crie um arquivo `.env` na mesma pasta do `app.py` com o conteúdo:

   OPENAI_API_KEY=coloque_sua_chave_aqui

3. Coloque sua chave da OpenAI no lugar de `coloque_sua_chave_aqui`.

4. Execute o app:

   ```powershell
   C:/Users/junio/develop/repos/IA-para-Devs/course/python-gpt-crie-chatbot-com-ia/lab1/venv/Scripts/python.exe app.py
   ```

5. Acesse no navegador: http://127.0.0.1:5000/

Pronto! Você pode conversar com o chatbot usando a API da OpenAI.
