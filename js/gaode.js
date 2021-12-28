var map=new AMap.Map("container",{
    zoom:11
});   

// 给起点和终点添加自动补全功能
new AMap.Autocomplete({
    input:"node1"
}) 
new AMap.Autocomplete({
    input:"node2"
}) 

btn.onclick=function(){
    //使用插件
    new AMap.Driving({
        map:map,
        panel:"panel"
    }).search([
        {keyword:node1.value,city:"宁波"},
        {keyword:node2.value,city:"宁波"}
    ],function(status,data){
        console.log(data);
    });
}
