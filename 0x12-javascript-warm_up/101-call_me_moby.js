#!/usr/bin/node
exports.callMeMoby = function (a, string) {
  for (let i = 0; i < a; i++) {
    string(a);
  }
}
