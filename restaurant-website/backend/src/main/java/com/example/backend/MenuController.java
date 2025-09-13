package com.example.backend;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class MenuController {
    @GetMapping("/api/hello")
    public String hello() {
        return "Welcome to the restaurant API!";
    }
}
