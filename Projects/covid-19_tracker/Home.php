<!DOCTYPE html>
<html>

<head>
    <title>CovidIndia</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- Latest compiled and minified CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css">
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

        @media only screen and (min-width: 480px) {
            .scrollLeft {

                display: none;
            }
        }
    </style>

</head>

<body>
    <?php include('navbar.html'); ?>
    <section class=" corona-update container-fluid">
        <div class="mb-4">
            <h2 class="text-center text-uppercase pt-3 pb-0">Main Dashboard</h2>
        </div>
    </section>


    <?php include('footer.html');  ?>
    <!-- jQuery library -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>

    <!-- Popper JS -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>

    <!-- Latest compiled JavaScript -->
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js"></script>
</body>

</html>