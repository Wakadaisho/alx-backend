import { createQueue } from 'kue';

const queue = createQueue()

const blacklist = ['4153518780', '4153518781']

function sendNotification(phoneNumber, message, job, done) {
    if (blacklist.includes(phoneNumber)) {
        return done(new Error(`Phone number ${phoneNumber} is blacklisted`))
    }
    job.progress(50, 50)
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
    done()
}

queue.process('push_notification_code_2', (job, done) => {
  job.progress(0, 50)
  sendNotification(job.data.phoneNumber, job.data.message, job, done);
  done()
});