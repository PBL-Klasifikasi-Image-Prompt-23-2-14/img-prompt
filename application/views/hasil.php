<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hasil Klasifikasi</title>
    <link rel="stylesheet" href="<?php echo base_url('assets/css/bootstrap.min.css'); ?>">
</head>
<body>
    <div class="container mt-5">
        <div class="alert alert-success text-center">
            <h4>Hasil Klasifikasi</h4>
            <p>Prediction: <?php echo $prediction; ?></p>
        </div>
    </div>
</body>
</html>
