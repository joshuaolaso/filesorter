
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Todo App</title>

    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/semantic-ui@2.4.2/dist/semantic.min.css">
    <script src="https://cdn.jsdelivr.net/npm/semantic-ui@2.4.2/dist/semantic.min.js"></script>
</head>

<body>
    <div style="margin-top: 50px;" class="ui container">
        <h1 class="ui center aligned header">To Do App</h1>

        <form class="ui form" action="/add" method="post">
            <div class="field">
                <label>Todo Title</label>
                <input type="text" name="title" placeholder="Enter Todo..."><br>
            </div>
            <button class="ui blue button" type="submit">Add</button>
        </form>

        <hr>

        {% for todo in todo_list %}
        <div class="ui segment">
            <p class="ui big header">{{todo.id }} | {{ todo.title }}</p>

            {% if todo.complete == False %}
            <span class="ui gray label">Not Complete</span>
            {% else %}
            <span class="ui green label">Completed</span>
            {% endif %}

            <a class="ui blue button" href="/update/{{ todo.id }}">Update</a>
            <a class="ui red button" href="/delete/{{ todo.id }}">Delete</a>
        </div>
        {% endfor %}
    </div>
</body>

</html>
