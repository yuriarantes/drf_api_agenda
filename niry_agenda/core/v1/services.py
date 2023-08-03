from datetime import datetime, timedelta, date

from ..models import Schedule, Scheduling, Store

class SchedulesServices:
    @classmethod
    def get_available_times(cls, store_id, date):
        try:
            schedules = []
            obj_schedule = Schedule.objects.filter(store=store_id,day=date.weekday()).first()

            time = obj_schedule.first_start_at

            if obj_schedule.last_end_at:
                last_time = obj_schedule.last_end_at
            else:
                last_time = obj_schedule.first_end_at

            while time < last_time:
                if obj_schedule.last_start_at:
                    if obj_schedule.first_end_at <= time < obj_schedule.last_start_at:
                        time = (datetime.combine(datetime.today(), time) + timedelta(minutes=30)).time()
                        continue
                    else:
                        pass
                
                if Scheduling.objects.filter(store=store_id, scheduling_date=datetime.combine(date, time)):
                    pass
                else:
                    schedules.append(time)

                time = (datetime.combine(datetime.today(), time) + timedelta(minutes=30)).time()

            return schedules
        except Exception as error:
            raise error
    