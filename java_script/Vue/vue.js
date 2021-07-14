// counter 

const Counter = {
    data() {
        return {
            counter: 0
        }
    },
    mounted() {
        setInterval(() => {
            this.counter++
        }, 1000)
    }
}
Vue.createApp(Counter).mount('#counter');
//--------------------------------------------------------------------------//

// v-bind attribute

const AttributeBinding = {
    data() {
        return {
            message: 'You loaded this page on ' + new Date().toLocaleString()
        }
    }
}
Vue.createApp(AttributeBinding).mount('#bind-attribute')
//----------------------------------------------------------------------------------//
// v-on directive

const EventHandling = {
    data() {
        return {
            message: 'Hello Vue.js!'
        }
    }, 
    methods: {
        reverseMessage() {
            this.message = this.message
            .split('')
            .reverse()
            .join('')
        }
    }
}
Vue.createApp(EventHandling).mount('#event-handling')
//-----------------------------------------------------------------//
// v-model directiv
const TwoWayBinding = {
    data() {
        return {
            message: 'Hello vue!'
        }
    }
}
Vue.createApp(TwoWayBinding).mount('#two-way-binding')
//---------------------------------------------------------------
// v-if ConditionalRendering

const ConditionalRendering = {
    data() {
        return {
            seen: true
        }
    }
}
Vue.createApp(ConditionalRendering).mount('#conditional-rendering')
//---------------------------------------------------------------
// v-for directive

const ListRendering = {
    data () {
        return {
            todos: [
                { text: 'learn Javascript'},
                { text: 'learn Vue'},
                { text: 'Build somthoing awesome'}
            ]
        }
    }
}
Vue.createApp(ListRendering).mount('#list-rendering')
//---------------------------------------------------------------
// Composing with components
const TodoList = {
    data() {
      return {
        groceryList: [
          { id: 0, text: 'Vegetables' },
          { id: 1, text: 'Cheese' },
          { id: 2, text: 'Whatever else humans are supposed to eat' }
        ]
      }
    }
  }
  
  const app = Vue.createApp(TodoList)
  
  app.component('todo-item', {
    props: ['todo'],
    template: `<li>{{ todo.text }}</li>`
  })
  
  app.mount('#todo-list-app')