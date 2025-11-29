import 'package:flutter/material.dart';

class PerfilCardPage extends StatelessWidget {
  const PerfilCardPage({super.key});

  @override
  Widget build(BuildContext context) {
    final colorScheme = Theme.of(context).colorScheme;

    return Scaffold(
      appBar: AppBar(
        title: const Text('Perfil'),
 
      ),
      body: Center(
        child: Container(
          padding: const EdgeInsets.all(25), 
          decoration: BoxDecoration(
            color: colorScheme.surface, 
            borderRadius: BorderRadius.circular(25), 
            boxShadow: [
              BoxShadow(
                color: colorScheme.primary.withOpacity(0.2), 
                blurRadius: 10,
                offset: const Offset(0, 5),
              ),
            ],
          ),
          width: 320, 
          child: Column(
            mainAxisSize: MainAxisSize.min,
            children: [
            
              CircleAvatar(
                radius: 45, 
                backgroundColor: colorScheme.primary, 
                child: const CircleAvatar(
                  radius: 42,
                  backgroundImage: NetworkImage('https://i.pravatar.cc/150?img=3'),
                ),
              ),
              const SizedBox(height: 15),
              const Text(
                'Derick Dutra',
                style: TextStyle(fontSize: 22, fontWeight: FontWeight.bold), 
              ),
              Text(
                '@DERICK',
                style: TextStyle(color: colorScheme.secondary), 
              ),
              const SizedBox(height: 25),
              Divider(color: colorScheme.outlineVariant), 
              const SizedBox(height: 15),
              Row(
                mainAxisAlignment: MainAxisAlignment.spaceAround,
                children: [
                  _buildStatColumn('Posts', '150', colorScheme.primary),
                  _buildStatColumn('Seguidores', '5140', colorScheme.primary),
                  _buildStatColumn('Seguindo', '1830', colorScheme.primary),
                ],
              ),
            ],
          ),
        ),
      ),
    );
  }

  
  Widget _buildStatColumn(String label, String value, Color color) {
    return Column(
      children: [
        Text(
          value,
          style: TextStyle(
            fontSize: 20,
            fontWeight: FontWeight.bold,
            color: color, 
          ),
        ),
        Text(
          label,
          style: TextStyle(color: Colors.grey[600]),
        ),
      ],
    );
  }
}