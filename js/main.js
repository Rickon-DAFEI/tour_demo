var app = new Vue({
    el: '.app',
    data: {
      message: 'Hello Vue!'
    },
    methods:{
        buy_ticket:function(){

            this.$router.push({ path:'/ticket.html'}) 
        }
    }
  })