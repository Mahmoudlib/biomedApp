from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Device, Company

def home_view(request):
    query = request.GET.get('q', '').strip()
    
    featured_devices = Device.objects.filter(is_featured=True)
    if not featured_devices.exists():
        featured_devices = Device.objects.all()[:2]
        
    popular_devices = Device.objects.all().order_by('-views_count')[:6]
    leader_companies = Company.objects.filter(is_leader=True)[:4]
    if not leader_companies.exists():
        leader_companies = Company.objects.all()[:4]

    context = {
        'featured_devices': featured_devices,
        'popular_devices': popular_devices,
        'leader_companies': leader_companies,
        'query': query,
        'active_tab': 'home',
    }
    return render(request, 'home.html', context)


def device_list_view(request):
    query = request.GET.get('q', '').strip()
    category = request.GET.get('category', '').strip()

    devices = Device.objects.all()

    if query:
        devices = devices.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(working_principle__icontains=query)
        )

    if category and category != 'Tous':
        devices = devices.filter(category__iexact=category)

    total_count = devices.count()
    categories = ['Tous', 'Laboratoire', 'Imagerie', 'Bloc opératoire', 'Cardiologie', 'Réanimation']

    context = {
        'devices': devices,
        'total_count': total_count,
        'categories': categories,
        'selected_category': category or 'Tous',
        'query': query,
        'active_tab': 'devices',
    }
    return render(request, 'devices/device_list.html', context)


def device_detail_view(request, pk):
    device = get_object_or_404(Device, pk=pk)
    # Increment view count
    Device.objects.filter(pk=pk).update(views_count=device.views_count + 1)
    device.refresh_from_db()

    # Split maintenance steps into clean lines if structured with numbers
    maintenance_steps = [
        step.strip() for step in device.maintenance_protocol.split('\n') if step.strip()
    ]

    context = {
        'device': device,
        'maintenance_steps': maintenance_steps,
        'active_tab': 'devices',
    }
    return render(request, 'devices/device_detail.html', context)


def company_list_view(request):
    query = request.GET.get('q', '').strip()
    region = request.GET.get('region', '').strip()

    companies = Company.objects.all()

    if query:
        companies = companies.filter(
            Q(name__icontains=query) |
            Q(specialization__icontains=query) |
            Q(description__icontains=query)
        )

    if region and region != 'Toutes':
        companies = companies.filter(region__iexact=region)

    regions = ['Toutes', 'Dakar', 'Thiès', 'Saint-Louis', 'Ziguinchor']

    context = {
        'companies': companies,
        'regions': regions,
        'selected_region': region or 'Toutes',
        'query': query,
        'active_tab': 'companies',
    }
    return render(request, 'companies/company_list.html', context)


def company_detail_view(request, pk):
    company = get_object_or_404(Company, pk=pk)
    related_companies = Company.objects.exclude(pk=pk)[:3]

    context = {
        'company': company,
        'related_companies': related_companies,
        'active_tab': 'companies',
    }
    return render(request, 'companies/company_detail.html', context)


def offline_view(request):
    return render(request, 'offline.html')
