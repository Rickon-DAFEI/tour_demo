var mySwiper = new Swiper ('.swiper-container', {
    
  // 轮播图的方向，也可以是vertical方向

  direction:'horizontal',

  //播放速度

  loop: true,

  // 自动播放时间

  autoplay:true,

  // 播放的速度

  speed:2000,

  // 如果需要分页器，即下面的小圆点

  pagination: {

  el: '.swiper-pagination',

  },

  　　// 这样，即使我们滑动之后， 定时器也不会被清除

  　　autoplayDisableOnInteraction : false,

  });
// var ticket = new Vue({
//   el: '.place_item',
//   data: {
//     message: 'Hello Vue!'
//   },
//   onload:function(){
    
  
//   },
//   methods:{
//   }
  
// })

var search = new Vue({
  el: '.hot_main',
  data: {
    message: 'Hello Vue!',
    places:[],
  },
  onload:function(){
    
  
  },
  mounted:function(){
    this.gethotplace();
  },
  methods:{
    gethotplace:function(){
      var that = this;
      post_data = {"req":"list"};
      axios.post('ticket.php', post_data)
          .then(function (response) {
              that.places = response["data"];
              // console.log(response["data"]);
              // alert("提交成功");
          })
          .catch(function (error) {

              // console.log(error);
          });
      
    }
  }
  
})