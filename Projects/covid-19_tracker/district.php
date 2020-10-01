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

		.search-box {
			border: solid #343A40 2px;

		}

		#India {
			width: 25px;

		}

		.corona-update h5 {
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
<?php include('navbar.html');  ?>
	<section class=" corona-update container-fluid">
		<div class="mb-4">
			<h2 class="text-center text-uppercase pt-3 pb-0">COVID-19 LIVE STATS-(India)</h2>
		</div>

		<!--SEARCH BOX-->
		<div class="text-center">
			<!--Search box-->
			<!-- <input class=" text-center mb-3 pl-5 pr-5 pt-2 pb-2 search-box" type="text" id="myInput" onkeyup="myFunction()" placeholder="Search for Districts.." title="Search here"> -->
			<form class="form-group" method="GET">
				<select onchange="this.form.submit();" name="state" id="myInput" required class="text-center mb-3 pl-5 pr-5 pt-2 pb-2 search-box">
					<option value="">Select State</option>
					<option value="Andhra Pradesh">Andhra Pradesh</option>
					<option value="Andaman and Nicobar Islands">Andaman and Nicobar Islands</option>
					<option value="Arunachal Pradesh">Arunachal Pradesh</option>
					<option value="Assam">Assam</option>
					<option value="Bihar">Bihar</option>
					<option value="Chandigarh">Chandigarh</option>
					<option value="Chhattisgarh">Chhattisgarh</option>
					<option value="Dadar and Nagar Haveli">Dadar and Nagar Haveli</option>
					<option value="Daman and Diu">Daman and Diu</option>
					<option value="Delhi">Delhi</option>
					<option value="Lakshadweep">Lakshadweep</option>
					<option value="Puducherry">Puducherry</option>
					<option value="Goa">Goa</option>
					<option value="Gujarat">Gujarat</option>
					<option value="Haryana">Haryana</option>
					<option value="Himachal Pradesh">Himachal Pradesh</option>
					<option value="Jammu and Kashmir">Jammu and Kashmir</option>
					<option value="Jharkhand">Jharkhand</option>
					<option value="Karnataka">Karnataka</option>
					<option value="Kerala">Kerala</option>
					<option value="Madhya Pradesh">Madhya Pradesh</option>
					<option value="Maharashtra">Maharashtra</option>
					<option value="Manipur">Manipur</option>
					<option value="Meghalaya">Meghalaya</option>
					<option value="Mizoram">Mizoram</option>
					<option value="Nagaland">Nagaland</option>
					<option value="Odisha">Odisha</option>
					<option value="Punjab">Punjab</option>
					<option value="Rajasthan">Rajasthan</option>
					<option value="Sikkim">Sikkim</option>
					<option value="Tamil Nadu">Tamil Nadu</option>
					<option value="Telangana">Telangana</option>
					<option value="Tripura">Tripura</option>
					<option value="Uttar Pradesh">Uttar Pradesh</option>
					<option value="Uttarakhand">Uttarakhand</option>
					<option value="West Bengal">West Bengal</option>
				</select>
			</form>
			<p>[Please avoid spaces after name]</p>
		</div>
	</section>
	<!--Access the data statewise from API-->
	<?php
	$x = 'https://api.covid19india.org/v2/state_district_wise.json';
	$ch = curl_init();
	curl_setopt($ch, CURLOPT_URL, $x);
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
	$districtdata = curl_exec($ch);
	curl_close($ch);
	$disdata = json_decode($districtdata, true); //decode it using json
	if (isset($_GET['state'])) {
		$ok = $_GET['state'];
		$output = '';
		$output .= '<section class=" corona-update container-fluid">
		         <div class="text-center table-responsive">
				<table class="table table-bordered table-striped table-dark" id="corona_table">
					<tr>
						<th scope="col">District</th>
						<th scope="col">Confirmed</th>
						<th scope="col">Active</th>
						<th scope="col">Recovered</th>
						<th scope="col">Death</th>
					</tr>
				<tbody>';
		foreach ($disdata as $key => $value) {
			if ($value['state'] == $ok) {
				//echo $state;
				for ($i = 0; $i < count($value['districtData']); $i++) {
					$output .= '<tr>
					<th>' . $value['districtData'][$i]['district'] . '</th>
					<td>' . $value['districtData'][$i]['confirmed'] . '</td>
					<td>' . $value['districtData'][$i]['active'] . '</td>
					<td>' . $value['districtData'][$i]['recovered'] . '</td>
					<td>' . $value['districtData'][$i]['deceased'] . '</td>
				</tr>';
					//print_r($value['districtData'][$i]['district']);
				}
				break;
			}
		}
		$output .= '</tbody></table></div></section>';
		echo $output;
	} 

	?>
	<?php include('footer.html');  ?>

	<!-- jQuery library -->
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>

	<!-- Popper JS -->
	<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>

	<!-- Latest compiled JavaScript -->
	<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js"></script>
</body>

</html>