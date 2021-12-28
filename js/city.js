
var city = new Vue({
    el: '.city',
    data: {
      message: 'Hello Vue!',
      city:'城市',
      banner_url:["img/10010h00000091zen97DB_D_769_510_Q100.jpg",
      "img/10070f0000007ksnk631C_D_769_510_Q100.jpg",
      "img/100i0j0000009ttb0AEDA_D_769_510_Q100.jpg",
      "img/100r0f0000007ks52FD01_D_769_510_Q100.jpg",
      "img/10030e00000077tj23C12_D_769_510_Q100.jpg"
    ],
    sells:[
      {
        sel_num:"31",
        h3:"上海东方明珠广播电视塔 （俯瞰浦江外滩美景/毗邻东方明珠 上海中心大厦）",
        span1:'体验悬空玻璃刺激',
        span2:'468米俯瞰脚下',
        span3:"标志性建筑",
        imgurl:'img/dfmzt.jpg',
        money:'30'
      },
      {
        sel_num:"31",
        h3:"上海东方明珠广播电视塔 （俯瞰浦江外滩美景/毗邻东方明珠 上海中心大厦）",
        span1:'体验悬空玻璃刺激',
        span2:'468米俯瞰脚下',
        span3:"标志性建筑",
        imgurl:'img/dfmzt.jpg',
        money:'30'
      }
    ]
    },
    onload(){
        
    },
    mounted(){
        this.getcity();
        this.get_banner();
        this.get_sells();
    },
    methods:{
      get_banner:function(){
        var that = this;
        post_data = {"req":"banner","city":that.city};
        axios.post('city.php', post_data)
            .then(function (response) {
                that.banner_url = response["data"];
            })
            .catch(function (error) {
  
                // console.log(error);
            });
        
      },
      get_sells:function(){
        var that = this;
        post_data = {"req":"sell","city":that.city};
        axios.post('sell.php', post_data)
            .then(function (response) {
                that.sells = response["data"];
                // console.log(response["data"]) ;
            })
            .catch(function (error) {
  
                // console.log(error);
            });
        
      },
      getcity:function(){
            var url = location.search; //获取url中"?"符后的字串
            if (url.indexOf("?") != -1) {
            var str = url.substr(1);
            strs = str.split("&");
            this.city = decodeURIComponent(strs[0].replace("city=",""));
        }
        
       } 
    }
    
  })