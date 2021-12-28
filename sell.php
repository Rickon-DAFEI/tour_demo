<?php

    include 'database.php';
    $content = file_get_contents('php://input');
    $post_data = json_decode($content,true);
    if($post_data["req"]=='sell'){
            $city = $post_data['city'];
            // $sql = "select id,time,place,detail,level,contact_person,contact_phone,photo_url,place_se,flag from report where openid='".$_SESSION['openid']."' order by time desc;";
            $sql = "select * from hot_buy_ticket where city_name = '".$city."' order by sell_num desc limit 6;";
            // echo $sql;
            $res = $conn->query($sql);
            $ans = array();
            if($res->num_rows > 0)
            {
                
                while($row = $res->fetch_assoc())
                {
                $ret = ["sell_num" => $row['sell_num'],"h3" => $row['detail'], "span1" => $row['span1'],'span2'=>$row['span2'],'span3'=>$row['span3'],'imgurl'=>$row['photo_url'],'money'=>$row['money']];
                array_push($ans, $ret);
                }
                echo json_encode($ans,JSON_UNESCAPED_UNICODE);
            }
            else{
            
            }
            $conn->close();
        }
        else{
            $city = "上海";
            // $sql = "select id,time,place,detail,level,contact_person,contact_phone,photo_url,place_se,flag from report where openid='".$_SESSION['openid']."' order by time desc;";
            $sql = "select * from hot_buy_ticket where city_name = '".$city."' order by sell_num desc limit 6;";
            // echo $sql;
            $res = $conn->query($sql);
            $ans = array();
            if($res->num_rows > 0)
            {
                
                while($row = $res->fetch_assoc())
                {
                $ret = ["sell_num" => $row['sell_num'],"h3" => $row['detail'], "span1" => $row['span1'],'span2'=>$row['span2'],'span3'=>$row['span3'],'imgurl'=>$row['photo_url'],'money'=>$row['money']];
                array_push($ans, $ret);
                }
                echo json_encode($ans,JSON_UNESCAPED_UNICODE);
            }
            else{
            
            }
            $conn->close();
        }

?>