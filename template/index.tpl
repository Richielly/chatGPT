<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Tela de Chat</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" integrity="sha384-eTN3qKr+b+sNSCUs28+kX9pJ6Fb+1v0gR/Cs/YsZdPA+pLcGJSZpzoFZLnU6OxU6" crossorigin="anonymous">
    <style>
        .olive-background {
            background-color: rgba(128, 128, 0, 0.2);
        }
        .orange-button {
            background-color: #FFA500;
            border-color: #FFA500;
        }
        .chat-container {
            max-width: 700px;
            border-radius: 10px;
            overflow: hidden;
        }
        .chat-header {
            background-color: #075E54;
            color: #fff;
            padding: 15px;
            font-size: 20px;
            font-weight: bold;
        }
        .chat-body {
            background-color: #F4F4F4;
            padding: 15px;
            min-height: 500px;
            max-height: 500px;
            overflow-y: auto;
        }
        .chat-message {
            display: flex;
            flex-direction: row;
            align-items: flex-end;
            margin-bottom: 10px;
        }
        .chat-message-avatar {
            width: 40px;
            height: 40px;
            border-radius: 50%;
            margin-right: 10px;
        }
        .chat-message-content {
            background-color: #fff;
            padding: 10px;
            border-radius: 10px;
            max-width: 70%;
            word-wrap: break-word;
        }
        .chat-message-content-user {
            background-color: #DCF8C6;
        }
        .chat-message-content-bot {
            background-color: #fff;
        }
        .chat-message-timestamp {
            font-size: 12px;
            margin-left: 10px;
        }
    </style>
</head>
<body>
    <div class="d-flex flex-column vh-100 olive-background">
        <div class="container-fluid h-100 my-auto">
            <div class="row justify-content-center align-items-center h-100">
                <div class="chat-container">
                    <div class="chat-header">Gpt Chat</div>
                    <div class="chat-body">
                        <div class="chat-message">
                            <img src="https://via.placeholder.com/40x40" alt="Avatar" class="chat-message-avatar">
                            <div class="chat-message-content chat-message-content-bot">
                                {{dados}}
                                <div class="chat-message-timestamp">{{hora}}</div>
                            </div>
                        </div>
                        <div class="chat-message">
                            <img src="https://via.placeholder.com/40x40" alt="Avatar" class="chat-message-avatar">
                            <div class="chat-message-content chat-message-content-user">
                                {{mensagem}}
                                <div class="chat-message-timestamp">{{hora}}</div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
          <div class="form-group">
            <label for="dados" class="col-form-label"></label>
            <input type="text" class="form-control" id="dados" name="dados">
          </div>
        </form>
</body>