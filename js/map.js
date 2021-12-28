
var myChart = echarts.init(document.getElementById('china-map'));  
function randomData() {
    return Math.round(Math.random() * 1000);
}

var data = [{
    name: '江苏省',
    value: 5.3
},
{
    name: '北京市',
    value: 3.8
},
{
    name: '上海',
    value: 4.6
},
{
    name: '重庆',
    value: 3.6
},
{
    name: '河北',
    value: 3.4
},
{
    name: '河南',
    value: 3.2
},
{
    name: '云南',
    value: 1.6
},
{
    name: '辽宁',
    value: 4.3
},
{
    name: '黑龙江',
    value: 1.3
},
{
    name: '湖南',
    value: 2.4
},
{
    name: '安徽',
    value: 3.3
},
{
    name: '山东',
    value: 3.0
},
{
    name: '新疆',
    value: 1
},
{
    name: '江苏',
    value: 3.9
},
{
    name: '浙江',
    value: 3.5
},
{
    name: '江西',
    value: 1.4
},
{
    name: '湖北',
    value: 2.1
},
{
    name: '广西',
    value: 3.0
},
{
    name: '甘肃',
    value: 1.2
},
{
    name: '山西',
    value: 3.2
},
{
    name: '内蒙古',
    value: 1.4
},
{
    name: '陕西',
    value: 2.5
},
{
    name: '吉林',
    value: 4.5
},
{
    name: '福建',
    value: 2.8
},
{
    name: '贵州',
    value: 1.8
},
{
    name: '广东',
    value: 3.7
},
{
    name: '青海',
    value: 0.6
},
{
    name: '西藏',
    value: 0.4
},
{
    name: '四川',
    value: 3.3
},
{
    name: '宁夏',
    value: 0.8
},
{
    name: '海南',
    value: 1.9
},
{
    name: '台湾',
    value: 2.3
},
{
    name: '香港',
    value: 0.1
},
{
    name: '澳门',
    value: 0.1
},
{
    name: '北京',
    value: 6.0
},
{
    name: '天津',
    value: 0.3
}
];

var yData = [];
var barData = [];
var placeData = [];
for (var i = 0; i < 10; i++) {
barData.push(data[i]);
yData.push(i + data[i].name);
}

var option = {
title: [{
    show: false,
    text: '排名情况',
    textStyle: {
        color: '#2D3E53',
        fontSize: 18
    },
    // right: 180,
    // top: 100
}],
// tooltip: {
//     show: false,
//     formatter: function(params) {
//         return params.name + '：' + params.data['value'] + '%'
//     },
// },
visualMap: {
    type: 'continuous',
    orient: 'horizontal',
    itemWidth: 10,
    itemHeight: 80,
    // text: ['高', '低'],
    showLabel: false,
    seriesIndex: [0],
    min: 0,
    max: 2,
    inRange: {
        color: ['#DCDCDC','#FFFFF0','#40E0D0', '#6A5ACD', '#FF0000']
    },
    textStyle: {
        color: '#7B93A7'
    },
    bottom: 30,
    left: 'left',
},

xAxis: {
    show: false
},
yAxis: {
    show:false,
    // type: 'category',
},
tooltip: {
    show: true,
    formatter: function(params) {
        return params.name + '：' + params.data['value'] + '%'
    },
},
geo: {
    // roam: true,
    
    map: 'china',
    left: 'left',
    right: '300',
    // layoutSize: '80%',
                        normal: {
                            show: true,//显示省份标签
                            textStyle:{color:"#fbfdfe"}//省份标签字体颜色
                        },    
    itemStyle: {
        emphasis: {
            areaColor: '#fff'
        }
    },
   
},
series: [{
    name: 'mapSer',
    type: 'map',
    roam: false,
    geoIndex: 0,
    label: {
        show: false,
        
    },
    data: data
}]
};
myChart.setOption(option);  
window.onresize=function(){
    myChart.resize();
} 
myChart.on('click', function (param){
    var name=param.name;
    for(i=0;i<data.length;i++){
        if(data[i].name==name){
            var index=i
        }
    }
    window.open('city.html?city='+name); 
            	
});
// myChart.on('click',eConsole);
