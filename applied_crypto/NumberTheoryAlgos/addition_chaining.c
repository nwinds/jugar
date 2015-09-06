// loop ver
unsigned long qe2(unsigned long x, unsigned long y, unsigned long n) {
	unsigned long s, t, u;
	int i;

	s = 1;
	t = x;
	u = y;
	while (u) {
		if (u & 1) {
			s = (s * t) % n;
		}
		u >>= 1;
		t = (t * t) % n;
	}
	return (s);
}

// recursive ver
unsigned long fast_exp(unsigned long x, unsigned long y, unsigned long N) {
	unsigned long tmp;
	if (y == 1) {
		return (x % N);
	}

	if ((y & 1) == 0) {
		tmp = fast_exp(x, y / 2, N);
		return ((tmp * tmp) % N);
	} else {
		tmp = fast_exp(x, (y - 1) / 2, N);
		tmp = (tmp * tmp) % N;
		tmp = (tmp % x) % N;
		return (tmp);
	}
}
