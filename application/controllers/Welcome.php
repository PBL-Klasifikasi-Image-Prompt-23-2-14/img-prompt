<?php
defined('BASEPATH') OR exit('No direct script access allowed');

class Welcome extends CI_Controller {

    public function __construct()
    {
        parent::__construct();
        $this->load->database();  // Load library database
    }

    public function index()
    {
        $this->load->view('welcome_message');
    }

    public function proses()
    {
        if(isset($_FILES['image'])){
            $image = $_FILES['image']['tmp_name'];
            $prompt = $this->input->post('prompt');

            $ch = curl_init();

            curl_setopt($ch, CURLOPT_URL, "http://localhost:5000/predict");
            curl_setopt($ch, CURLOPT_POST, 1);
            curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
            curl_setopt($ch, CURLOPT_POSTFIELDS, [
                'image' => new CURLFile($image)
            ]);

            $response = curl_exec($ch);
            curl_close($ch);

            $response_data = json_decode($response, true);

            if(isset($response_data['prediction'])){
                $prediction = $response_data['prediction'];
                // Simpan hasil ke database
                $data = [
                    'prompt' => $prompt,
                    'prediction' => $prediction
                ];
                $this->db->insert('klasifikasi', $data);  // Pastikan ini menggunakan $this->db
                $this->load->view('hasil', ['prediction' => $prediction]);
            } else {
                echo "Error: " . $response_data['error'];
            }
        }
    }
}
