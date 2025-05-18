import http from 'k6/http';
import { check } from 'k6';

export let options = {
  stages: [
    { duration: '1m', target: 10 },
    { duration: '3m', target: 50 },
    { duration: '2m', target: 30 },
    { duration: '5m', target: 50 },
    { duration: '30s', target: 0 },
  ],
  thresholds: {
    http_req_duration: ['p(95)<2000'],
    http_req_failed: ['rate<0.01'],
  },
};

const urls = [
  'https://bongau.edu.et/registrar-office',
];

export default function () {
  urls.forEach(url => {
    const res = http.get(url);
    check(res, {
      [`${url} - status 200`]: (r) => r.status === 200,
      [`${url} - response < 2s`]: (r) => r.timings.duration < 2000,
    });
  });
}
