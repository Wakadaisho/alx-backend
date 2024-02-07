function createPushNotificationsJobs(jobs, queue) {
    if (!Array.isArray(jobs)) throw new Error('Jobs is not an array');

    const jobQueues = jobs.map((jobData) => {
        const job = queue.create('push_notification_code_3', jobData).save((err) => {
            if (!err) console.log(`Notification job created: ${job.id}`)
        });

        job.on('complete', () => {
            console.log(`Notification job ${job.id} completed`)
        })
        job.on('failed', (err) => {
            console.log(`Notification job ${job.id} failed: ${err}`)
        })
        job.on('progress', (prog) => {
            console.log(`Notification job #${job.id} ${prog}% complete`)
        })
        return job;
    })
    return jobQueues;
}

export default createPushNotificationsJobs;
