<?php

    include 'database.php';


    $content = file_get_contents('php://input');
    $post_data = json_decode($content,true);
    if($post_data["req"]=='list'){
        // $sql = "select id,time,place,detail,level,contact_person,contact_phone,photo_url,place_se,flag from report where openid='".$_SESSION['openid']."' order by time desc;";
        $sql = "select name from hot_place;";
        $res = $conn->query($sql);
        $ans = array();
        if($res->num_rows > 0)
        {
            
            while($row = $res->fetch_assoc())
            {
              $name = $row["name"];
               
                array_push($ans, $name);
            } 
            echo json_encode($ans,JSON_UNESCAPED_UNICODE);
        }
        $conn->close();
    }

?>