#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (err, _response, body) {
  if (err) {
    console.error(err);
  } else {
    const todoComplete = {};
    body = JSON.parse(body);

    for (let i = 0; i < body.length; ++i) {
      const userId = body[i].user_id;
      const completedTasks = body[i].completed_tasks;

      if (!todoComplete[userId] && completedTasks) {
        todoComplete[userId] = 0;
      }
      i++;
    }
    console.log(todoComplete);
  }
});
