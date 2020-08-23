This is a PHP file from https://github.com/Buscatrufas/UrbanRivals/blob/master/index.php

It has been modified to work with the new HTTPS urls, as well as demonstrate how to work with functions.

To run PHP, you need a web server. An easy one to set up is XAAMP. Details at https://www.techomoro.com/how-to-run-a-php-application-on-windows-10-using-xampp/

Given the above, you need to put this file under `xaamp/htdocs`. Then in your browser simply type "localhost" and it should pop up. If there is already an `index.php` in your `htdocs`, it makes more sense to put this one under a subfolder of `htdocs`, like `urbanrivals`. In this case you use your browser to navigate to `localhost/urbanrivals`

XAAMP by default uses port 80 and routes to `index.php`. If you name the file differently, you need to specify the name in the url. If the file name is `php_example.php` and is placed under the `xaamp/htdocs/urbanrivals` folder, you need to use your browser to navigate to `localhost/urbanrivals/php_example.php`