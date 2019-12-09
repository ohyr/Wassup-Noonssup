module.exports = {
    HTML:function(customer_photo, eyebrow1, eyebrow2, eyebrow3, celeb1, celeb2, celeb3){
        return `
        <!DOCTYPE html>
<html>
<head>
  <link rel='stylesheet' href='/stylesheets/style.css' />
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Wassup Noonssup</title>

  <!-- 부트스트랩 -->
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css">
  <style>
    /* jumbotron */
    .jumbotron{
      background-image: url("https://cdn.pixabay.com/photo/2017/08/13/18/47/eye-2638202__340.jpg");
      background-size: cover;
      text-shadow: black 0.2em 0.2em 0.2em;
      color: white;
      height: fit-content;
    }

    #customer_photo{
      max-width: 100%;
      height: auto;
    }

    .descript{
      height: 70px;
    }

    #photo_list, #photo_list_eyebrow{
      overflow: auto;
      white-space: nowrap;
      height: 200px;
    }

    #img1, #img2{
      max-width: 120px;
      height: auto;
    }

    #img3{
      max-width: 120px;
      height: auto;
    }

    #img1_eyebrow, #img2_eyebrow, #img3_eyebrow{
      max-width: 120px;
      height: auto;
    }

    .padding1{
      height: 30px;
    }

    .radio-items{
      padding-left: 25%;
    }
    
    #custom_id, #main_img_eyebrow{
      max-width: 95%;
      height: 450px;
    }
    
    #main_img{
      max-width: 95%;
      height: auto;
    }
    
    .holder{
      height: 450px;
    }
    
    .img_holder{
      height: 450px;
    }
    
    .btn{
      color: lightyellow;
    }

    </style>
</head>

<body>
<nav class="navbar navbar-inverse navbar-fixed-top">
  <div class="container">
    <div class="navbar-header">
      <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
        <span class="sr-only">Toggle navigation</span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
      </button>
      <a class="navbar-brand" href="/">Wassup Noonssup</a>
    </div>
    <div id="navbar" class="navbar-collapse collapse">
    </div>
  </div>
</nav>

<!-- Main jumbotron for a primary marketing message or call to action -->
<div class="jumbotron">
  <div class="container">
    <h1>Wassup Noonsup</h1>
    <p>You can be more beautiful than you are now. <br>If you upload your image, we will find you a suitable eyebrow shape.
      <br>Be beautiful easily.</p>
    <p><a class="btn btn-light btn-lg" href="/" role="button">Home &raquo;</a></p>
  </div>
</div>

<div class="container">
  <!-- Example row of columns -->
  <div class="row">
<!--    화면의 3분의 1만 사용-->
    <div class="col-md-4">
      <article>
        <center>
        <div class="descript"><h2>Photo you uploaded</h2></div>
        <div id="holder">
            <img id="custom_id" src="${customer_photo}">
        </div>
        <div class="padding1"></div>
        </center>
      </article>
      <script>
        var upload = document.getElementsByTagName('input')[0],
                holder = document.getElementById('holder');
        var main_num = 1;
        var main_num_eyebrow = 1;

        upload.onchange = function (e) {
          e.preventDefault();

          var file = upload.files[0],
                  reader = new FileReader();
          reader.onload = function (event) {
            var img = new Image();
            img.src = event.target.result;
            img.id = 'customer_photo'
            if (img.width > 300) { // holder width
              img.width = 300;
            }
            holder.innerHTML = '';
            holder.appendChild(img);
          };
          reader.readAsDataURL(file);

          return false;
        };

        function change_img_eyebrow(num) {
          if(main_num_eyebrow != num){
            $("#main_img_eyebrow").attr("src", jQuery('#img' + num + '_eyebrow').attr("src"));
            main_num_eyebrow = num;
          }
        }

        function change_img(num) {
          if(main_num != num){
            $("#main_img").attr("src", jQuery('#img' + num).attr("src"));
            main_num = num;
          }
        }

      </script>
    </div>

<!--    합성된 눈썹 사진 보여줄 부분-->
    <div class="col-md-4">
      <center>
      <div class="descript"><h2>Eyebrow Recommendation</h2></div>
      <div class="img_holder"><img id="main_img_eyebrow" src="${eyebrow1}"></div>
      <div class="padding1"></div>
      <div id="photo_list_eyebrow">
        <img id="img1_eyebrow" onclick="change_img_eyebrow(1)" src="${eyebrow1}">
        <img id="img2_eyebrow" onclick="change_img_eyebrow(2)" src="${eyebrow2}">
        <img id="img3_eyebrow" onclick="change_img_eyebrow(3)" src="${eyebrow3}">
      </div>
      </center>
    </div>


<!--    합성할 연예인 사진 보여줄 부분-->
    <div class="col-md-4">
      <center>
      <div class="descript"><h2>A recommended face </h2></div>
      <div class="img_holder"><img id="main_img" src="${celeb1}"></div>
      <div class="padding1"></div>
      <div id="photo_list">
        <img id="img1" onclick="change_img(1)" src="${celeb1}">
        <img id="img2" onclick="change_img(2)" src="${celeb2}">
        <img id="img3" onclick="change_img(3)" src="${celeb3}">
      </div>
      </center>
    </div>

  </div>

  <hr>

  <footer>
    <p>&copy; 2019 집중교육 9조</p>
  </footer>
</div>
<!-- /container -->
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/js/bootstrap.min.js"></script>
</body>

</html>
        `;
    }
};