package main

import (
	"bufio"
	"fmt"
	"os"
)

func testcase() {
	
}

func main() {
	defer outf.Flush()

	var t int = 1
	in(&t)

	for t > 0 {
		t--
		testcase()
		out("\n")
	}
}

var (
	inf  = bufio.NewReader(os.Stdin)
	outf = bufio.NewWriter(os.Stdout)
)

func in[T any](i *T) {
	fmt.Fscan(inf, i)
}

func out[T any](i T) {
	fmt.Fprint(outf, i)
}

func b2i(exp bool) int {
	if exp {
		return 1
	}
	return 0
}

func i2b(exp int) bool {
	if exp == 0 {
		return false
	}
	return true
}

func ternary[T any](cond bool, v1 T, v2 T) T {
	if cond {
		return v1
	} else {
		return v2
	}
}