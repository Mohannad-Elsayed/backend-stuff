package main

import (
	"encoding/json"
	"fmt"
	// "log"
)

type User struct {
	Name string `json:"name"`
	Age  int    `json:"age"`
}

func main() {
	u := new(User)
	u.Name = "hehehehe"
	u.Age = 21
	data, err := json.Marshal(u)
	if err != nil {
		// log.Fatal(err)
	}
	fmt.Println(string(data))
}
