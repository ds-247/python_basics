import pymongo;
from bson import ObjectId

client = pymongo.MongoClient('mongodb+srv://<user>:<pass>@vidlycluster.rw7lwml.mongodb.net/',  tlsAllowInvalidCertificates=True)
# client = pymongo.MongoClient('mongodb+srv://<username>:<pass>@vidlycluster.rw7lwml.mongodb.net/'pymongo)
db = client['pymongo']

video_collection = db['videos'];


def list_all_videos() : 
    resp = video_collection.find({});
    for video in video_collection.find() :
        print(f"video_id {video['_id']} , video_name {video['name']} , video_duration {video['time']}");

def add_video(duration, name) :
    video_collection.insert_one({'name' : name, 'time' : duration});

def update_video(video_id, duration, name):
    try:
        video_collection.update_one({'_id': ObjectId(video_id)}, {'$set': {"name": name, 'time': duration}})
        print("Video updated successfully!")
    except Exception as e:
        print("Error updating video:", e)

def delete_video(video_id) : 
    video_collection.delete_one({'_id' : ObjectId(video_id)})

def main() :
    print("main function is executed",video_collection);

    while 1 :
        print("\n Youtube Video Managing App | Choose an option");
        print("1. List all youtube videos ")
        print("2. Add a youtube video ");
        print("3. Update a youtube video details ");
        print("4. Delete a youtube video ");
        print("5. Exit the app");
        choice = input("Enter your choice : ");

        if choice == '1' :
            list_all_videos();
        elif  choice == '2':
            name = input("Enter name of video ... ")
            time = input("Enter the duration of video ... ");
            add_video(duration=time, name=name)
        elif choice == '3' :
            list_all_videos();
            video_id = input("enter the video_id : ");
            name = input('enter the new name : ');
            time = input("enter the new duration : ");
            update_video(video_id= video_id, name=name, duration=time);
        elif choice == '4' :
            video_id = input("enter the video id to be deleted  : ")
            delete_video(video_id);
        elif  choice == '5':
            break;
        else :
            print("Invalid selection ... ")

if __name__ == '__main__' :
    main();