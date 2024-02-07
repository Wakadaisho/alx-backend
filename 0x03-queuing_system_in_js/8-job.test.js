import createPushNotificationsJobs from "./8-job";
import kue from 'kue';
import { expect } from "chai";


const queue = kue.createQueue();


describe('createPushNotificationsJobs', () => {
    before(function() {
        queue.testMode.enter();
      });
      
      afterEach(function() {
        queue.testMode.clear();
      });
      
      after(function() {
        queue.testMode.exit()
      });

    it('createPushNotificationsJobs', () => {
        const list = [
        {
            phoneNumber: '4153518780',
            message: 'This is the code 1234 to verify your account'
        }
        ];
        createPushNotificationsJobs(list, queue);
        expect(queue.testMode.jobs.length).to.equal(1);
    });
});