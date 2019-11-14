<?php
   $destino="conyguz99@gmail.com";
   $nombre= $_POST["name"];
   $correo= $_POST["email"];
   $telefono= $_POST["phone"];
   $mensaje= $_POST["message"];
   //concatenar todos los atributos
   $contenido= "Nombre: " . $nombre "\nCorreo: " . $correo . "\nTeléfono: " . $telefono . "\nMensaje: " . $mensaje;
   //crear el mensaje para que llegue al email
   mail($destino, "Contacto Fotografía", $contenido);
   
?>