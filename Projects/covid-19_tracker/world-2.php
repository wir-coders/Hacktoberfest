<?php
$ch = curl_init();
curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

if (isset($_GET['country']) && !empty($_GET['country'])) {

    curl_setopt($ch, CURLOPT_URL, 'https://covid19.mathdro.id/api/countries/' . urlencode($_GET['country']));
    $result = curl_exec($ch);
    $data = json_decode($result, true);
}
?>
<!doctype html>
<html lang="en">

<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">

    <title>CovidIndia</title>
    <link href="https://fonts.googleapis.com/css2?family=Muli:wght@300&display=swap" rel="stylesheet">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Muli', sans-serif;

        }

        .line {
            text-decoration: underline;
        }

        .search-box {
            border: solid #343A40 2px;
        }

        .corona-update h5 {
            text-decoration: underline;
        }

        @media only screen and (min-width: 480px) {
            .scrollLeft {
                display: none;
            }
        }

        ::-webkit-scrollbar {
            display: none;
        }
    </style>
</head>

<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark d-flex justify-content-center">
        <h1 class="navbar-brand line" href="#">COVID-19 LIVE STATS (World)</h1>
        <h6 style="color:#fff;">Developed by Aman05382</h6>
    </nav>
    <section class=" corona-update container-fluid">
        <div class="mb-4">
            <h2 class="text-center text-uppercase pt-3 pb-0">COVID-19 LIVE STATS-(World)</h2>
        </div>
    </section>
    <br>
    <!--SEARCH BOX-->
    <div class="text-center">
        <!--Search box-->
        <form class="form-group" method="get">
            <input name="country" class=" text-center mb-3 pl-5 pr-5 pt-2 pb-2 search-box" type="text" id="myInput" onkeyup="myFunction()" placeholder="Search for countries.." title="Search here">
            <button type="submit" id="aman" class="btn btn-dark">Search</button>
        </form>
    </div>
    <?php if (!empty($data['confirmed'])) : ?>

        <!-- All World Data-->
        <div class="mb-4">
            <h2 class="text-center text-uppercase pt-3 pb-0">Showing Statistics of <?php echo htmlspecialchars($_GET['country'], ENT_QUOTES); ?></h2>
        </div>

        <section class="container-fluid">
            <div class="row" style="text-align: center">
            
                <div class="col-lg-2 col-md-2 col-12"></div>

                <div class="col-lg-2 col-md-2 col-12">
                    <h5 class="font-weight-bold">Total confirmed</h5>
                    <h3 class="count pb-2" id="TC"><?php echo number_format($data['confirmed']['value']) ?></h3>
                </div>


                <div class="col-lg-2 col-md-2 col-12">
                    <h5 class="font-weight-bold">Total recovered</h5>
                    <h3 class="count pb-2" id="TR"><?php echo number_format($data['recovered']['value']) ?></h3>
                </div>

                <div class="col-lg-2 col-md-2 col-12">
                    <h5 class="font-weight-bold">Total deaths</h5>
                    <h3 class="count pb-2" id="TD"><?php echo number_format($data['deaths']['value']) ?></h3>
                </div>

                <div class="col-lg-2 col-md-2 col-12">
                    <h5 class="font-weight-bold">Last update</h5>
                    <h3 class="count pb-2" id="LU"><?php echo $data['lastUpdate'] ?></h3>
                </div>
            </div>
        </section>
    <?php endif; ?>
    <hr>
    <div class="text-xs-center text-lg-center">
        <img src='https://covid19.mathdro.id/api/og' height="500px" width="auto" />
    </div>
    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
</body>

</html>