const Todo = {
    data () {
      return {
        todos: [],
        newTodo: ''
      }
    },
    computed: {
      completed () {
        return this.todos.filter(todo => todo.completed)
      },
      incomplete () {
        return this.todos.filter(todo => !todo.completed)
      }
    },
    methods: {
      addTodo () {
        const todo = { text: this.newTodo, completed: false }
        this.todos.push(todo)
      },
      removeTodo (todo) {
        const index = this.todos.indexOf(todo)
        this.todos.splice(index, 1)
      },
      completeTodo (todo) {
        const index = this.todos.indexOf(todo)
        this.todos[index].completed = true
      }
    }
  }
  const app = Vue.createApp(Todo)
  app.component('todo-item', {
    props: ['todo', 'removeTodo', 'completeTodo'],
    template: `<li>
      {{ todo.text }}
      <button v-on:click="removeTodo(todo)">remove</button>
      <button v-if="!todo.completed" v-on:click="completeTodo(todo)">complete</button>
    </li>`
  })
  app.mount('#todo')