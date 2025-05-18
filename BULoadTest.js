import http from 'k6/http';
import { check, sleep } from 'k6';

export let options = {
  vus: 100,          // 100 virtual users
  duration: '1m',    // run test for 1 minute
};

export default function () {
  let res = http.get('https://bongau.edu.et/');

  check(res, {
    'status is 200': (r) => r.status === 200,
    'response time < 1s': (r) => r.timings.duration < 1000,
  });

  sleep(1); 
}
