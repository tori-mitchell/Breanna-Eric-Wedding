// Daily schedules (one per day, timestamps instead of dates).
// PLACEHOLDER DATA: every time and event below is a dummy example, not the real schedule. Replace before launch (docs/CONTENT-TODO.md).
// Set to true to show each day's hourly rows. While false, each day shows its heading and image plus a "Details coming soon" note.
export const showDailyRows = false;

export const daily = [
  { title: 'Arrival', date: 'Thursday the 16th', img: 'images/art/arrival.jpg', imgLabel: 'Watercolor: villa arrival', rows: [
    { time: '3:00 PM', title: 'Placeholder 1', desc: 'Dummy text. Not the real schedule.' },
    { time: '5:30 PM', title: 'Placeholder 2', desc: 'Dummy text. Not the real schedule.' },
    { time: '7:30 PM', title: 'Placeholder 3', desc: 'Dummy text. Not the real schedule.' },
  ] },
  { title: 'Relaxation', date: 'Friday the 17th', img: 'images/art/pool-party.jpg', imgLabel: 'Watercolor: pool terrace', rows: [
    { time: '9:00 AM', title: 'Placeholder 1', desc: 'Dummy text. Not the real schedule.' },
    { time: '12:30 PM', title: 'Placeholder 2', desc: 'Dummy text. Not the real schedule.' },
    { time: '6:00 PM', title: 'Placeholder 3', desc: 'Dummy text. Not the real schedule.' },
  ] },
  { title: 'Wedding Day', date: 'Saturday the 18th', img: 'images/art/ceremony.jpg', imgLabel: 'Watercolor: ceremony', rows: [
    { time: '10:00 AM', title: 'Placeholder 1', desc: 'Dummy text. Not the real schedule.' },
    { time: '4:00 PM', title: 'Placeholder 2', desc: 'Dummy text. Not the real schedule.' },
    { time: '7:00 PM', title: 'Placeholder 3', desc: 'Dummy text. Not the real schedule.' },
  ] },
  { title: 'Departure', date: 'Sunday the 19th', img: 'images/art/terrace-cafe-crop.jpg', soft: true, imgLabel: 'Watercolor: morning coffee on the terrace', rows: [
    { time: '8:30 AM', title: 'Placeholder 1', desc: 'Dummy text. Not the real schedule.' },
    { time: '11:00 AM', title: 'Placeholder 2', desc: 'Dummy text. Not the real schedule.' },
  ] },
];
